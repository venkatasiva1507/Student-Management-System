document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("student-form");

    if (form) {
        form.addEventListener("submit", function (event) {
            const name = form.elements["name"].value.trim();
            const email = form.elements["email"].value.trim();
            const phone = form.elements["phone"].value.trim();
            const course = form.elements["course"].value.trim();

            if (!name || !email || !phone || !course) {
                event.preventDefault();
                alert("Please fill in all student details.");
                return;
            }

            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                event.preventDefault();
                alert("Please enter a valid email address.");
                return;
            }

            if (phone.length > 15) {
                event.preventDefault();
                alert("Phone number must be at most 15 characters.");
            }
        });
    }
});