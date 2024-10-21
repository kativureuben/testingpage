function scrollToContact() {
    window.scrollTo({
        top: document.querySelector('.contact').offsetTop,
        behavior: 'smooth'
    });
}

document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    this.reset();
});
