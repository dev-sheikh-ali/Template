document.addEventListener("DOMContentLoaded", function() {
    // Initialize the Flowbite modal manually if needed
    const modalElement = document.getElementById('logoutModal');
    if (modalElement) {
        const modal = new Modal(modalElement);
    }

    // Logout Modal Toggle
    document.querySelectorAll("[data-modal-toggle='logoutModal']").forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const modal = document.getElementById('logoutModal');
            if (modal) {
                modal.classList.remove('hidden');
                modal.setAttribute('aria-hidden', 'false');
                modal.setAttribute('role', 'dialog');
                modal.setAttribute('aria-modal', 'true');
            }
        });
    });

    // Confirm Logout - Submit Logout Form
    const confirmLogoutBtn = document.getElementById('confirmLogoutBtn');
    if (confirmLogoutBtn) {
        confirmLogoutBtn.addEventListener('click', function(event) {
            event.preventDefault();
            const logoutForm = document.getElementById('logoutForm');
            if (logoutForm) {
                logoutForm.submit(); // Submit the form to perform the logout
            }
        });
    }

    // Closing Modals
    document.querySelectorAll("[data-modal-hide]").forEach(function(button) {
        button.addEventListener('click', function() {
            const modal = button.closest('.modal');
            if (modal) {
                modal.classList.add('hidden');
                modal.setAttribute('aria-hidden', 'true');
                modal.removeAttribute('role');
                modal.removeAttribute('aria-modal');
            }
        });
    });
});
