import { useState } from "react";
import Input from "../Input/Input";
import styles from "./Layout.module.css";
import Card from "../Card/Card";
import { motion } from "motion/react";

export const animation = {
  hidden: {
    opacity: 0,
    height: 0,
  },
  visiable: () => ({
    opacity: 1,
    height: "auto",
    transition: {
      delay: 1,
      duration: 1,
    },
  }),
};

export default function Layout() {
  const [isSearch, setIsSearch] = useState(false);

  return (
    <section className={`${styles.layout} ${isSearch ? styles.search : " "}`}>
      <h1 className={`${styles.title} ${isSearch ? styles.hideTitle : " "}`}>
        ВВЕДИТЕ ОПИСАНИЕ СОТРУДНИКА
      </h1>

      <Input isSearch={isSearch} setIsSearch={setIsSearch} />
      {isSearch && (
        <motion.div initial="hidden" animate="visiable" variants={animation}>
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
        </motion.div>
      )}
    </section>
  );
}
