import Input from "../Input/Input";
import styles from "./Layout.module.css";

export default function Layout() {
  return (
    <section className={styles.layout}>
      <h1 className={styles.title}>ВВЕДИТЕ ОПИСАНИЕ СОТРУДНИКА</h1>
      <Input />
    </section>
  );
}
