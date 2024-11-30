import styles from "./Card.module.css";
import defaultAvatar from "../../assets/defaultAvatar.svg";

interface CardProps {
  setPopup: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function Card({ setPopup }: CardProps) {
  return (
    <div className={styles.card}>
      <div className={styles.displayFlex}>
        <img src={defaultAvatar} alt="avatar" className={styles.icon}></img>
        <div>
          <h2 className={styles.name}>Обимпе</h2>
          <h3 className={styles.age}>
            22 года{" "}
            <li className={styles.sick}>
              <span>На больничном с 29.11.2024 до 31.11.2077</span>
            </li>
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
        <button
          className={styles.button}
          onClick={() => {
            setPopup(true);
          }}
        >
          ПОДРОБНЕЕ
        </button>
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
            <p
              className={styles.text + " " + styles.master}
              onClick={() => {
                setPopup(true);
              }}
            >
              Мацегора Виктор Николаевич
            </p>
          </div>
        </div>
        <hr className={styles.line}></hr>
      </div>
    </div>
  );
}
