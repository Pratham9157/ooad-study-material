(function () {
  // theme
  var root = document.documentElement;
  if (localStorage.getItem('ooad-theme') === 'dark') root.classList.add('dark');
  var tt = document.getElementById('toggleTheme');
  if (tt) tt.onclick = function () {
    root.classList.toggle('dark');
    localStorage.setItem('ooad-theme', root.classList.contains('dark') ? 'dark' : 'light');
  };
  // show / hide all answers
  var ta = document.getElementById('toggleAns'), shown = false;
  if (ta) {
    if (!document.querySelector('details.ans')) ta.style.display = 'none';
    ta.onclick = function () {
      shown = !shown;
      document.querySelectorAll('details.ans').forEach(function (d) { d.open = shown; });
      ta.textContent = shown ? 'Hide all answers' : 'Show all answers';
    };
  }
  // copy buttons on C++ code
  document.querySelectorAll('.codewrap.cpp').forEach(function (w) {
    var b = document.createElement('button');
    b.className = 'copybtn'; b.textContent = 'copy';
    b.onclick = function () {
      navigator.clipboard.writeText(w.querySelector('pre').innerText);
      b.textContent = 'copied!'; setTimeout(function () { b.textContent = 'copy'; }, 1200);
    };
    w.appendChild(b);
  });
})();
