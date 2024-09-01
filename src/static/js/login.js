async function loginUser(event) {
    event.preventDefault(); // Prevent the default form submission
    const formData = new FormData(event.target);

    const response = await fetch('/auth/token', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (response.ok) {
        localStorage.setItem('access_token', result.access_token);
        window.location.href = '/dashboard';
    } else {
        alert(result.detail);
    }
}