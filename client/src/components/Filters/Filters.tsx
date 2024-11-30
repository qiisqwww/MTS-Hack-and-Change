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
        <Filter title="Подразделение №3" />
        <Filter title="Подразделение №4" />
        <Filter title="Должность" />
        <Filter title="Роль" />
        <Filter title="Фамилия" />
        <Filter title="Имя" />
        <Filter title="Телефон" />
        <Filter title="Город" />
        <Filter title="Адрес" />
        <Filter title="Почта" />
      </ul>
      <button className={styles.submit}>ПРИМЕНИТЬ</button>
      <button className={styles.reset}>СБРОСИТЬ</button>
    </div>
  );
}
