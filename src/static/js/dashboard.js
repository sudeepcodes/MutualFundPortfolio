async function fetchFunds() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('You are not logged in.');
        window.location.href = '/login';
        return;
    }

    try {
        const response = await fetch('/funds', {
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
        const fundSelect = document.getElementById('fund_name');
        fundSelect.innerHTML = ''; // Clear existing options

        result.funds.forEach(fund => {
            const option = document.createElement('option');
            option.value = fund;
            option.textContent = fund;
            fundSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching funds:', error);
    }
}

async function selectFund() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('You are not logged in.');
        window.location.href = '/login';
        return;
    }

    const formData = new FormData(document.querySelector('form'));

    try {
        const response = await fetch('/funds/select', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        });

        if (response.status === 401) {
            // Token is expired
            alert('Session expired. Please log in again.');
            localStorage.removeItem('access_token');
            window.location.href = '/login';
            return;
        }

        const result = await response.json();
        const tableBody = document.getElementById('funds_table_body');
        tableBody.innerHTML = ''; // Clear existing table data

        result.funds.forEach(fund => {
            const row = document.createElement('tr');
            row.innerHTML = `
                    <td>${fund.Scheme_Code}</td>
                    <td>${fund.ISIN_Div_Payout_ISIN_Growth}</td>
                    <td>${fund.ISIN_Div_Reinvestment}</td>
                    <td>${fund.Scheme_Name}</td>
                    <td>${fund.Net_Asset_Value}</td>
                    <td>${fund.Date}</td>
                    <td>${fund.Scheme_Type}</td>
                    <td>${fund.Scheme_Category}</td>
                    <td>${fund.Mutual_Fund_Family}</td>
                    <td><input type="number" id="quantity_${fund.Scheme_Name}" name="units" min="1" value="1"></td> <!-- Quantity input -->
                    <td><button onclick="buyFund('${fund.Scheme_Name}')">Buy</button></td>
                `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error selecting fund:', error);
    }
}

async function buyFund(fundName) {
    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('You are not logged in.');
        window.location.href = '/login';
        return;
    }

    const quantityInput = document.getElementById(`quantity_${fundName}`);
    const units = quantityInput.value;

    // Validate units input
    if (!units || units <= 0) {
        alert('Please enter a valid quantity.');
        return;
    }

    const formData = new URLSearchParams();
    formData.append('fund_name', fundName);
    formData.append('units', units);

    try {
        const response = await fetch('/funds/buy', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData.toString()
        });

        if (response.status === 401) {
            // Token is expired
            alert('Session expired. Please log in again.');
            localStorage.removeItem('access_token');
            window.location.href = '/login';
            return;
        }

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error buying fund:', error);
    }
}

async function goToPortfolio() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        alert('You are not logged in.');
        window.location.href = '/login';
        return;
    }

    // Redirect to portfolio page
    window.location.href = '/portfolio';
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

window.onload = fetchFunds;
