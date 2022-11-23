using System.Drawing;
using UnityEngine;

public class Rain : MonoBehaviour
{
    public MeshRenderer renderer;
    public float minX, maxX, minZ, maxZ, newX, newY, newZ;

    // Start is called before the first frame update
    void Start()
    {
        renderer = gameObject.GetComponent<MeshRenderer>();
        minX = renderer.bounds.min.x;
        maxX = renderer.bounds.max.x;

        minZ = renderer.bounds.min.z;
        maxZ = renderer.bounds.max.z;
    }

    // Update is called once per frame
    void Update()
    {
        newX = Random.Range(minX, maxX);
        newZ = Random.Range(minZ, maxZ);
        newY = gameObject.transform.position.y + 20;

        if (Input.GetKeyUp(KeyCode.N))
        {
            GameObject newCube = GameObject.CreatePrimitive(PrimitiveType.Cube);
            newCube.transform.position = new Vector3(newX, newY, newZ);
            newCube.AddComponent<Rigidbody>();
        }
    }

    public void OnCollisionEnter(Collision collision)
    {
        collision.gameObject.GetComponent<Rigidbody>().AddExplosionForce(1000, collision.contacts[0].point, 100);
    }
}
