import { useState } from "react";

const RebalanceButton = ({ portfolio }) => {
  const [adjustments, setAdjustments] = useState(null);

  const handleRebalance = async () => {
    const response = await fetch("http://localhost:8000/rebalance", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(portfolio),
    });
    const data = await response.json();
    setAdjustments(data.adjustments);
  };

  return (
    <div>
      <button onClick={handleRebalance}>Rebalance Portfolio</button>
      {adjustments && (
        <pre>{JSON.stringify(adjustments, null, 2)}</pre>
      )}
    </div>
  );
};

export default RebalanceButton;
