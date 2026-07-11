/*==================================================
    Employee Salary Analytics
    animation.js
==================================================*/

/* ==========================================
   Scroll Reveal
========================================== */

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
      }
    });
  },
  {
    threshold: 0.2,
  },
);

document.querySelectorAll(".fade-up").forEach((el) => {
  observer.observe(el);
});

document.querySelectorAll(".fade-left").forEach((el) => {
  observer.observe(el);
});

document.querySelectorAll(".fade-right").forEach((el) => {
  observer.observe(el);
});

/* ==========================================
   Counter Animation
========================================== */

const counters = document.querySelectorAll("[data-counter]");

const animateCounter = (counter) => {
  const target = Number(counter.dataset.counter);

  let value = 0;

  const speed = target / 80;

  const update = () => {
    value += speed;

    if (value < target) {
      counter.innerText = Math.floor(value);

      requestAnimationFrame(update);
    } else {
      counter.innerText = target;
    }
  };

  update();
};

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);

      counterObserver.unobserve(entry.target);
    }
  });
});

counters.forEach((counter) => {
  counterObserver.observe(counter);
});

/* ==========================================
   Smooth Scroll
========================================== */

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute("href"));

    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
      });
    }
  });
});
