#!/usr/bin/env python3
import json
import os
import copy
from typing import Dict, List, Set, Any

def get_current_schema() -> Dict:
    """Load the current docs.json schema"""
    with open('docs.json', 'r') as f:
        return json.load(f)

def dir_to_title(dir_name: str) -> str:
    """Convert directory name to title case for display
    
    Examples:
        get-started -> Get Started
        client-reference -> Client Reference
        api-reference -> API Reference
    """
    # Special case for API
    if dir_name.lower() == 'api-reference':
        return 'API Reference'
    
    # Split by hyphens and capitalize each word
    words = dir_name.split('-')
    return ' '.join(word.capitalize() for word in words)

def scan_directory(dir_path: str) -> List[str]:
    """
    Scan a directory for markdown files and return paths
    """
    markdown_files = []
    
    if not os.path.exists(dir_path):
        print(f"Warning: Directory {dir_path} does not exist")
        return []
    
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mdx') or file.endswith('.md'):
                # Get path relative to workspace
                rel_path = os.path.join(root, file)
                
                # Remove file extension
                rel_path = os.path.splitext(rel_path)[0]
                markdown_files.append(rel_path)
    
    return sorted(markdown_files)

def get_existing_paths(schema: Dict) -> Set[str]:
    """Extract all page paths from the existing schema"""
    paths: Set[str] = set()
    
    def extract_paths_recursive(item: Any) -> None:
        """Extract paths recursively from nested structures"""
        if isinstance(item, str):
            paths.add(item)
        elif isinstance(item, dict) and 'pages' in item:
            for page in item['pages']:
                extract_paths_recursive(page)
        elif isinstance(item, list):
            for page in item:
                extract_paths_recursive(page)
    
    # Extract from navigation structure
    for tab in schema.get('navigation', {}).get('tabs', []):
        for group in tab.get('groups', []):
            extract_paths_recursive(group.get('pages', []))
    
    return paths

def add_new_files_to_schema(schema: Dict, all_files: List[str]) -> Dict:
    """Add new files to schema, preserving the existing structure"""
    # Create a deep copy to avoid modifying the original
    updated_schema = copy.deepcopy(schema)
    
    # Get paths in the current schema
    existing_paths = get_existing_paths(schema)
    
    # Find new paths (files that don't exist in the schema)
    new_files = [f for f in all_files if f not in existing_paths]
    
    if not new_files:
        print("No new files to add to the schema.")
        return schema
    
    print(f"Found {len(new_files)} new files to add to the schema:")
    for f in new_files:
        print(f"  - {f}")
    
    # Group new files by their prefix (aurelio-sdk or semantic-router)
    sdk_files = [f for f in new_files if f.startswith('aurelio-sdk')]
    router_files = [f for f in new_files if f.startswith('semantic-router')]
    
    # Add new files to the schema
    for tab in updated_schema.get('navigation', {}).get('tabs', []):
        if tab.get('tab') == 'Aurelio SDK' and sdk_files:
            add_files_to_tab(tab, sdk_files)
        elif tab.get('tab') == 'Semantic Router' and router_files:
            add_files_to_tab(tab, router_files)
    
    return updated_schema

def add_files_to_tab(tab: Dict, new_files: List[str]) -> None:
    """Add new files to a tab, trying to match them with existing patterns"""
    # Group files by likely category
    file_categories: Dict[str, List[str]] = {}
    
    # Use conservative mapping to match files to categories
    for file in new_files:
        parts = file.split('/')
        
        # Default to "Uncategorized" group
        category = "Uncategorized"
        
        if len(parts) >= 2:
            # Get the second part of the path (first directory after the tab name)
            dir_name = parts[1]
            
            # Special cases first
            if dir_name == 'introduction' or dir_name == 'quickstart':
                category = "Get Started"
            elif 'api-reference' in parts and len(parts) >= 5:
                # API reference files like "aurelio-sdk/api-reference/v1/chunk/post"
                category = "API Reference"
            else:
                # Convert directory name to title case for the category
                category = dir_to_title(dir_name)
        
        file_categories.setdefault(category, []).append(file)
    
    # Add files to groups
    for category, files in file_categories.items():
        # Find or create appropriate group
        target_group = None
        
        for group in tab.get('groups', []):
            if group.get('group') == category:
                target_group = group
                break
        
        if not target_group:
            # Create new group
            target_group = {'group': category, 'pages': []}
            tab.get('groups', []).append(target_group)
        
        # Handle API Reference specially - it has nested structure
        if category == "API Reference":
            add_to_api_reference_group(target_group, files)
        elif category == "Client Reference":
            add_to_client_reference_group(target_group, files)
        else:
            # Add to group directly
            target_group.get('pages', []).extend(files)
            # Keep pages sorted
            if all(isinstance(p, str) for p in target_group.get('pages', [])):
                target_group['pages'] = sorted(target_group['pages'])

def add_to_api_reference_group(group: Dict, files: List[str]) -> None:
    """Add files to API Reference group, which has nested structure"""
    # Group files by resource type (e.g., "chunk")
    resource_groups: Dict[str, List[str]] = {}
    
    for file in files:
        parts = file.split('/')
        if len(parts) >= 5:  # Expect pattern like 'aurelio-sdk/api-reference/v1/chunk/post'
            resource_type = parts[3]
            # Convert resource type to title case
            resource_title = dir_to_title(resource_type)
            resource_groups.setdefault(resource_title, []).append(file)
    
    pages = group.get('pages', [])
    
    # Find or create subgroups
    for resource_title, resource_files in resource_groups.items():
        # Find existing subgroup
        subgroup = None
        for page in pages:
            if isinstance(page, dict) and page.get('group') == resource_title:
                subgroup = page
                break
        
        if not subgroup:
            # Create new subgroup
            subgroup = {'group': resource_title, 'pages': []}
            pages.append(subgroup)
        
        # Add files to subgroup
        subgroup.get('pages', []).extend(resource_files)
        # Keep pages sorted
        subgroup['pages'] = sorted(subgroup['pages'])

def add_to_client_reference_group(group: Dict, files: List[str]) -> None:
    """Add files to Client Reference group, which might have deeply nested structure"""
    # For complex reference structures, use a more conservative approach
    
    # First, handle files at the top level of client reference
    top_level_files = []
    nested_files: Dict[str, List[str]] = {}
    
    for file in files:
        parts = file.split('/')
        if len(parts) <= 3:  # Simple path like 'semantic-router/client-reference/route'
            top_level_files.append(file)
        else:
            # Group nested files by their subdirectory
            # Path format: "semantic-router/client-reference/encoders/azure_openai"
            subdir = parts[2]  # e.g., "encoders" from the above example
            nested_files.setdefault(subdir, []).append(file)
    
    # Add top-level files directly
    if top_level_files:
        group.get('pages', []).extend(top_level_files)
    
    # For nested files, find or create appropriate subgroups
    for subdir, subdir_files in nested_files.items():
        # Find existing subgroup
        pages = group.get('pages', [])
        
        # Convert to title case for display
        subdir_title = dir_to_title(subdir)
        
        # Find matching subgroup
        subgroup = None
        for page in pages:
            if isinstance(page, dict) and page.get('group') == subdir_title:
                subgroup = page
                break
        
        if not subgroup:
            # Create new subgroup
            subgroup = {'group': subdir_title, 'pages': []}
            pages.append(subgroup)
        
        # Add files to subgroup
        subgroup.get('pages', []).extend(subdir_files)
        # Keep pages sorted
        if all(isinstance(p, str) for p in subgroup.get('pages', [])):
            subgroup['pages'] = sorted(subgroup['pages'])

def update_docs_schema():
    """
    Main function to update the docs.json schema
    """
    try:
        # Get the current schema
        current_schema = get_current_schema()
        
        # Scan directories for all markdown files
        all_files = scan_directory('aurelio-sdk') + scan_directory('semantic-router')
        
        # Add new files to schema
        updated_schema = add_new_files_to_schema(current_schema, all_files)
        
        # Write updated schema back to docs.json
        with open('docs.json', 'w') as f:
            json.dump(updated_schema, f, indent=2)
        
        print("docs.json has been updated successfully!")
    except Exception as e:
        print(f"Error updating docs.json: {e}")
        raise

if __name__ == "__main__":
    update_docs_schema() 