import Filter from "../Filter/Filter";
import Title from "../Title/Title";
import styles from "./Filters.module.css";

export default function Filters() {
  return (
    <div className={styles.filters}>
      <Title title="КРИТЕРИИ ПОИСКА" />
      <ul className={styles.list}>
        <Filter title="Подразделение №1" />
        <Filter title="Функциональный блок" />
        <Filter title="Подразделение №2" />
      </ul>
    </div>
  );
}
