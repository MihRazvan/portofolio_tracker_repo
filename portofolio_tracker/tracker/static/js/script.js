import React, { useState, useEffect } from 'react';

function ReactApp() {
    const [cryptoData, setCryptoData] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch(
                    `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=24h`
                );
                if (!response.ok) {
                    throw new Error('Failed to fetch data');
                }
                const data = await response.json();
                setCryptoData(data);
            } catch (error) {
                setError(error.message);
            }
        }
        fetchData();
    }, []);

    const filteredCryptoData = cryptoData.filter((crypto) =>
        crypto.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div>
            <h1>Cryptocurrency Tracker</h1>
            <input
                type="text"
                value={searchQuery}
                onChange={(event) => setSearchQuery(event.target.value)}
                placeholder="Search for a cryptocurrency..."
            />
            {error ? (
                <p>{error}</p>
            ) : (
                <ul>
                    {filteredCryptoData.map((crypto) => (
                        <li key={crypto.id}>
                            <img src={crypto.image} alt={crypto.name} />
                            <h2>{crypto.name}</h2>
                            <p>Price: ${crypto.current_price.toFixed(2)}</p>
                            <p>24h Change: {crypto.price_change_percentage_24h.toFixed(2)}%</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default ReactApp;