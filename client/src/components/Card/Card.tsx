import styles from "./Card.module.css";
import defaultAvatar from "../../assets/defaultAvatar.svg";

export default function Card() {
  return (
    <div className={styles.card}>
      <div className={styles.displayFlex}>
        <img src={defaultAvatar} alt="avatar" className={styles.icon}></img>
        <div>
          <h2 className={styles.name}>Обимпе</h2>
          <h3 className={styles.age}>
            22 года <span>bobo</span>
          </h3>
          <div className={styles.displayFlex}>
            <div className={styles.job}>
              <p>Тестировщик</p>
            </div>
            <div className={styles.role}>
              <p>Тестирование</p>
            </div>
          </div>
        </div>
        <button className={styles.button}>ПОДРОБНЕЕ</button>
      </div>
      <div>
        <div className={styles.grid}>
          <h4 className={styles.point}>Контакты</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>+7 888 888 88 88</p>
            <p className={styles.text}>mail@mail.ru</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Подразделения</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>центральный офис</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Функц. блок</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>Корпоративный блок</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Адрес офиса</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>
              г. Мариуполь, проспект Мира, 14, 5 этаж, офис 666
            </p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Руководитель</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>Мацегора Виктор Николаевич</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
      </div>
    </div>
  );
}
