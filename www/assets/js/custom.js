// Add any custom JavaScript here.
function showMap() {
  $('#tab-mapview').click();
}
setTimeout(showMap, 300);

var $installCard = $('#app-install-card').closest('.card').parent(),
    $supportedInstructions = $installCard.find('#app-install-button'),
    $nonsupportedInstructions = $installCard.find('#installation-instructions-button');

$installCard.hide();
$installCard.addClass('hide-after-install');
$supportedInstructions.hide();
$nonsupportedInstructions.hide();


if ('onbeforeinstallprompt' in window) {

  let deferredPrompt;

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
  });

  document.getElementById('app-install-button').addEventListener('click', (e) => {
    try {
      deferredPrompt.prompt();
    }
    catch (error) {
      // If this failed, the app must have already been installed.
      $supportedInstructions.replaceWith('<p class="already-installed">You have successfully installed the app.</p>');
    }
  });

  $installCard.show();
  $supportedInstructions.show();
}
else {
  $installCard.show();
  $nonsupportedInstructions.show();
}
