async function fetchPortfolio() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('You are not logged in.');
        window.location.href = '/login';
        return;
    }

    try {
        const response = await fetch('/users/portfolio', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.status === 401) {
            // Token is expired
            alert('Session expired. Please log in again.');
            localStorage.removeItem('access_token');
            window.location.href = '/login';
            return;
        }

        const result = await response.json();
        const portfolioTableBody = document.getElementById('portfolio_table_body');
        portfolioTableBody.innerHTML = ''; // Clear existing table data

        for (const [fund_name, units] of Object.entries(result.portfolio)) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${fund_name}</td>
                <td>${units}</td>
            `;
            portfolioTableBody.appendChild(row);
        }
    } catch (error) {
        console.error('Error fetching portfolio:', error);
    }
}

async function goToDashboard() {
    window.location.href = '/dashboard';
}

async function logout() {
    try {
        const response = await fetch('/auth/logout', {
            method: 'POST',
            credentials: 'include'
        });

        if (response.ok) {
            localStorage.removeItem('access_token');
            window.location.href = '/login';
        } else {
            alert('Logout failed');
        }
    } catch (error) {
        console.error('Error during logout:', error);
    }
}

window.onload = fetchPortfolio;
