using UnityEngine;
using UnityEngine.SceneManagement;

public class NextLevel : MonoBehaviour
{
    public void Next()
    {
        SceneManager.LoadScene("Level1");
        //Application.LoadLevel("Level1");
    }
}