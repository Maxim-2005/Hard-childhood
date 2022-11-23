using UnityEngine;

public class MyScript : MonoBehaviour
{
    [SerializeField]
    public int x, y;

    //Выполняется до запуска
    void Awake()
    {
        MyFunction();
    }

    //Выполняется при загрузки сцены
    void Start()
    {
        print("Hello World!");
    }

    //Выполняется при смене кадра
    void Update()
    {
        //print("X: " + x++ + " Время " + Time.deltaTime);
    }

    //Выполняется по таймеру
    void FixedUpdate()
    {
        //print("Y: " + y++ + " Время " + Time.deltaTime);
    }

    //Моя функция
    void MyFunction()
    {
        print("Hello World");
    }
}
