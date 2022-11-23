using UnityEngine;

public class MoveCube : MonoBehaviour
{
    public GameObject MyCube;
    float Delta = 50;

    // Update is called once per frame
    void Update()
    {
        Delta = Input.GetAxis("Horizontal") * 50;

        //Двигаем кубик
        //MyCube.transform.position = new Vector3(100 + Delta, 20, 100);

        //Красный
        if (Input.GetKeyUp(KeyCode.R))
            MyCube.GetComponent<Renderer>().material.color = Color.red;
        //Зеленый
        if (Input.GetKeyUp(KeyCode.G))
            MyCube.GetComponent<Renderer>().material.color = Color.green;
        //Синий
        if (Input.GetKeyUp(KeyCode.B))
            MyCube.GetComponent<Renderer>().material.color = Color.blue;

        //Сокрытие
        if (Input.GetKeyUp(KeyCode.Z))
            MyCube.SetActive(false);
        //Вскрытие
        if (Input.GetKeyUp(KeyCode.X))
            MyCube.SetActive(true);

        //удаление
        if (Input.GetKeyUp(KeyCode.Escape))
            Destroy(MyCube);

        //Вращение куба
        if (Input.GetKeyUp(KeyCode.UpArrow))
            MyCube.transform.Translate(Vector3.forward*Delta*Time.deltaTime);

        //Вращение куба
        if (Input.GetKeyUp(KeyCode.DownArrow))
            MyCube.transform.Translate(-Vector3.forward * Delta * Time.deltaTime);

        //Вращение куба
        if (Input.GetKeyUp(KeyCode.LeftArrow))
            MyCube.transform.Rotate(Vector3.up, Delta * Time.deltaTime);

        //Вращение куба
        if (Input.GetKeyUp(KeyCode.RightArrow))
            MyCube.transform.Rotate(Vector3.up, -Delta + Time.deltaTime);
    }       
}
