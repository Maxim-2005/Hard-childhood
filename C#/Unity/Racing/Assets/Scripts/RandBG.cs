using UnityEngine;

public class RandBG : MonoBehaviour
{
    public Material[] materials;
    void Start()
    {
        GetComponent<Skybox>().material = materials[Random.Range (0, materials.Length)];
    }      
}
