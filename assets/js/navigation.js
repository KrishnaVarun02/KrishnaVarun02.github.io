/* Native details/summary works without JS. These are optional keyboard conveniences. */
document.addEventListener('keydown', function (event) {
  if (event.key !== 'Escape') return;
  var openMenus = Array.from(document.querySelectorAll('.masthead details[open]'));
  var focusedMenu = openMenus.find(function (menu) { return menu.contains(document.activeElement); });
  openMenus.forEach(function (menu) { menu.open = false; });
  if (focusedMenu) focusedMenu.querySelector('summary').focus();
});
document.addEventListener('click', function (event) {
  document.querySelectorAll('.masthead details[open]').forEach(function (menu) {
    if (!menu.contains(event.target)) menu.open = false;
  });
});
