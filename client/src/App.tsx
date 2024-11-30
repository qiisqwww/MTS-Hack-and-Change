import { QuestionCircleOutlined } from "@ant-design/icons";
import "./App.css";
import Footer from "./components/Footer/Footer";
import Layout from "./components/Layout/Layout";
import LeftBoard from "./components/LeftBoard/LeftBoard";
import { Popover } from "antd";

const content = (
  <div style={{ padding: 10 }}>
    <p style={{ margin: 0 }}>
      В строке ввода сообщения введите известную информацию
      <br /> о сотруднике, которая могла бы быть в пункте "О себе". Так
      <br /> же, вы можете использовать критерии для поиска, чтобы
      <br /> сузить выдачу анкет.
    </p>
  </div>
);

function App() {
  return (
    <>
      <main className="main">
        <LeftBoard />
        <Layout />
        <div className="question">
          <Popover content={content}>
            <QuestionCircleOutlined className="question-icon" />
          </Popover>
        </div>
      </main>
      <Footer />
    </>
  );
}

export default App;
