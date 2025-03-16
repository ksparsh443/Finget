import { useState, useEffect } from "react";

const StockAlerts = ({ symbol }) => {
  const [price, setPrice] = useState("Waiting for updates...");

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${symbol}`);
    ws.onmessage = (event) => setPrice(event.data);
    ws.onerror = () => setPrice("Error fetching stock data.");
    return () => ws.close();
  }, [symbol]);

  return (
    <div>
      <h2>Live Stock Alerts: {symbol}</h2>
      <p>{price}</p>
    </div>
  );
};

export default StockAlerts;
