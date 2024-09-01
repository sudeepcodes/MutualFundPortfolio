async function registerUser(event) {
    event.preventDefault(); // Prevent the default form submission
    const formData = new FormData(event.target);

    const response = await fetch('/users/register', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    alert(result.message);

    if (response.ok) {
        window.location.href = '/users/login'; // Redirect to login page
    }
}