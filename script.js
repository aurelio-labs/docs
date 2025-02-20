function updatePageStyles() {
  const currentPath = window.location.pathname;
  if (currentPath.startsWith("/semantic-router")) {
    document.body.classList.add("semantic-router");
    document.body.classList.remove("aurelio-sdk");
  } else if (currentPath.startsWith("/aurelio-sdk")) {
    document.body.classList.remove("semantic-router");
    document.body.classList.add("aurelio-sdk");
  }
}

updatePageStyles();

const debounce = (func, delay) => {
  let timerId;
  return function (...args) {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
};

const debouncedUpdatePageStyles = debounce(() => {
  updatePageStyles();
}, 100);

const observer = new MutationObserver(function (mutations) {
  mutations.forEach(function (mutation) {
    if (mutation.type === "childList") {
      try {
        debouncedUpdatePageStyles();
      } catch (error) {
        console.error(error);
      }
    }
  });
});

observer.observe(document.body, { childList: true, subtree: true });
