import "./App.css";
import Footer from "./components/Footer/Footer";
import Layout from "./components/Layout/Layout";
import LeftBoard from "./components/LeftBoard/LeftBoard";

function App() {
  return (
    <>
      <main className="main">
        <LeftBoard />
        <Layout />
      </main>
      <Footer />
    </>
  );
}

export default App;
