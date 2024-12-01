import { QuestionCircleOutlined } from "@ant-design/icons";
import "./App.css";
import Footer from "./components/Footer/Footer";
import Layout from "./components/Layout/Layout";
import LeftBoard from "./components/LeftBoard/LeftBoard";
import { ConfigProvider, Popover } from "antd";
import { useState } from "react";
import { MPopup } from "./components/Popup/Popup";
// import { create } from "zustand";
// import { IPreson } from "./interfaces/IPerson";
// import { useTheme } from "./hooks/useTheme";

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

// eslint-disable-next-line react-refresh/only-export-components
export const animatePopup = {
  hidden: {
    opacity: 0,
  },
  visiable: () => ({
    opacity: 1,
    transition: {
      duration: 0.3,
    },
  }),
  exit: {
    opacity: 0,
    transition: {
      duration: 0.3,
      ease: "easeInOut",
    },
  },
};

function App() {
  const [popup, setPopup] = useState(false);
  // const { theme, setTheme } = useTheme();

  return (
    <ConfigProvider
      theme={{
        components: {
          Switch: {
            handleSize: 25,
            trackPadding: 3,
            trackHeight: 31,
            trackMinWidth: 71,
          },
        },
      }}
    >
      {popup && (
        <MPopup
          setPopup={setPopup}
          initial="hidden"
          animate="visiable"
          exit="exit"
          variants={animatePopup}
        />
      )}
      <main className="main">
        <LeftBoard />
        <Layout setPopup={setPopup} />
        <div className="question">
          <Popover content={content}>
            <QuestionCircleOutlined className="question-icon" />
          </Popover>
        </div>
      </main>
      <Footer />
    </ConfigProvider>
  );
}

export default App;
