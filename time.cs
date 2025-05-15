using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;

public class time : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {

    }
    [RuntimeInitializeOnLoadMethod]
    public static void GetTime()
    {
        Scene currentScene = SceneManager.GetActiveScene();
        string currentTime = System.DateTime.Now.ToString("hh:mm:ss");
        string ffTime = System.DateTime.Now.ToString("-hhmmss");
        string currentDate = System.DateTime.Now.ToString("MM/dd/yyyy");
        string ffDate = System.DateTime.Now.ToString("MMddyyyy");

        Variables.Scene(currentScene).Set("DateString", currentDate);
        Variables.Scene(currentScene).Set("TimeString", currentTime);
        Variables.Scene(currentScene).Set("filefriendlytime", ffTime);
        Variables.Scene(currentScene).Set("filefriendlydate", ffDate);

    }
    // Update is called once per frame
    void Update()
    {
        GetTime();
    }
}
