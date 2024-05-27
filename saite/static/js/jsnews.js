var lastScrollY = window.scrollY || window.pageYOffset;
var ticking = false;

function onScroll() {
    var header = document.querySelector('header');
    var heroText = document.getElementById('heroText');
    var image2 = document.getElementById('image2');
    var scrollY = window.scrollY || window.pageYOffset;
    var heroImageHeight = document.querySelector('.hero-image').offsetHeight;

    var startOffset = 20;
    var endOffset = heroImageHeight - 20 - heroText.offsetHeight;

    var newTop = startOffset + scrollY;
    if (newTop > endOffset) {
        newTop = endOffset;
    }

    heroText.style.top = newTop + 'px';

    var image2Start = 50;
    var image2End = 170;
    var image2Opacity = (scrollY - image2Start) / (image2End - image2Start);
    image2Opacity = Math.min(Math.max(image2Opacity, 0), 1);
    image2.style.opacity = image2Opacity;

    if (scrollY > 0) {
        header.classList.add('shadow');
    } else {
        header.classList.remove('shadow');
    }

    lastScrollY = scrollY;
    ticking = false;
}

function requestTick() {
    if (!ticking) {
        requestAnimationFrame(onScroll);
        ticking = true;
    }
}

window.addEventListener('scroll', requestTick);
document.addEventListener('DOMContentLoaded', onScroll);
