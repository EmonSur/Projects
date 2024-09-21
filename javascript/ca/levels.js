let level1Button = document.getElementById('level-1');
let level2Button = document.getElementById('level-2');
let level3Button = document.getElementById('level-3');
let level4Button = document.getElementById('level-4');

level1Button.addEventListener('click', function() {
    window.location.href = 'level1.html';
});

level2Button.addEventListener('click', function() {
    alert('Level 2 is locked! Complete Level 1 to unlock.');
});

level3Button.addEventListener('click', function() {
    alert('Level 3 is locked! Complete Level 2 to unlock.');
});

level4Button.addEventListener('click', function() {
    alert('Level 4 is locked! Complete Level 3 to unlock.');
});

