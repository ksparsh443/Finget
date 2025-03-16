import { useState } from "react";

function App() {
  const [plan, setPlan] = useState("");

  const fetchPlan = async () => {
    const response = await fetch("http://localhost:8000/plan/user1");
    const data = await response.json();
    setPlan(data.plan);
  };

  return (
    <div>
      <h1>WealthBot</h1>
      <button onClick={fetchPlan}>Get Investment Plan</button>
      <p>{plan}</p>
    </div>
  );
}

export default App;
