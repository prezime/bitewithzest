(async () => {
    if (navigator.brave) {
      if (await navigator.brave.isBrave()) {
        console.log(true);
      };
    } else {
      console.log(false);
    }
  })();  