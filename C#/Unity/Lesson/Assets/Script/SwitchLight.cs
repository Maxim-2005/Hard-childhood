using UnityEngine;

public class SwitchLight : MonoBehaviour
{
    private Light MyLight;

    // Start is called before the first frame update
    void Start()
    {
        MyLight = GetComponent<Light>();
    }

    // Update is called once per frame
    void Update()
    {
        //Включить/Отключить
        if (Input.GetKeyUp(KeyCode.Space))
            MyLight.enabled = !MyLight.enabled;
;
    }
}
