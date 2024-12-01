import styles from "./Card.module.css";
import defaultAvatar from "../../assets/defaultAvatar.svg";
import { IPreson } from "../../interfaces/IPerson";

interface CardProps {
  setPopup: React.Dispatch<React.SetStateAction<boolean>>;
  card: IPreson;
}

export default function Card({ setPopup, card }: CardProps) {
  return (
    <div className={styles.card}>
      <div className={styles.displayFlex}>
        <img src={defaultAvatar} alt="avatar" className={styles.icon}></img>
        <div>
          <h2 className={styles.name}>
            {card.first_name} {card.last_name}
          </h2>
          <h3 className={styles.age}>
            22 года{" "}
            <li className={styles.sick}>
              <span>На больничном с 29.11.2024 до 31.11.2077</span>
            </li>
          </h3>
          <div className={styles.displayFlex}>
            <div className={styles.job}>
              <p>{card.post}</p>
            </div>
            <div className={styles.role}>
              <p>{card.role}</p>
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
            <p className={styles.text}>{card.phone_number}</p>
            <p className={styles.text}>{card.email}</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Подразделения</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>{card.department_name}</p>
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
            <p className={styles.text}>{card.address}</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4
            className={styles.point + " " + styles.master}
            onClick={() => {
              setPopup(true);
            }}
          >
            Руководитель
          </h4>
        </div>
        <hr className={styles.line}></hr>
      </div>
    </div>
  );
}
