import Filter from "../Filter/Filter";
import Title from "../Title/Title";
import styles from "./Filters.module.css";

export default function Filters() {
  return (
    <div className={styles.filters}>
      <Title title="КРИТЕРИИ ПОИСКА" />
      <ul className={styles.list}>
        <Filter title="Подразделение №1" isList={true} />
        <Filter title="Функциональный блок" isList={true} />
        <Filter title="Подразделение №2" isList={true} />
        <Filter title="Подразделение №3" isList={true} />
        <Filter title="Подразделение №4" isList={true} />
        <Filter title="Должность" isList={true} />
        <Filter title="Роль" isList={true} />
        <Filter title="Фамилия" isList={false} />
        <Filter title="Имя" isList={false} />
        <Filter title="Телефон" isList={false} />
        <Filter title="Город" isList={false} />
        <Filter title="Адрес" isList={false} />
        <Filter title="Почта" isList={false} />
        <Filter title="Telegram" isList={false} />
      </ul>
      <button className={styles.submit}>ПРИМЕНИТЬ</button>
      <button className={styles.reset}>СБРОСИТЬ</button>
    </div>
  );
}
