import StockAlerts from "../components/StockAlerts";
import RebalanceButton from "../components/RebalanceButton";
export default function Home() {
    const samplePortfolio = { stocks: 7000, bonds: 2000, cash: 1000 };
  return (
    <div>
      <h1>WealthBot - Live Alerts</h1>
      <StockAlerts symbol="AAPL" />
   

       
      <h1>WealthBot - Portfolio Rebalancing</h1>
      <RebalanceButton portfolio={samplePortfolio} />
    </div>
  );
}
