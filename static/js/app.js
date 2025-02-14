document.querySelectorAll('.fadeButton').forEach(function(button) {
    button.addEventListener('click', function() {
        this.classList.add('fade-out');

        const url = this.getAttribute('data-url');

        setTimeout(function() {
            window.location.href = url;         
        }, 1000);
    });
});