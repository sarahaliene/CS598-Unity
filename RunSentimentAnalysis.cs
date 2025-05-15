using UnityEngine;
using UnityEditor.Scripting.Python;
using UnityEditor;
using Unity.VisualScripting;
using UnityEngine.SceneManagement;
using System.IO;
using System;

public class RunSentimentAnalysis : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {

    }

    [MenuItem("Python/Sentiment Analysis")]
    public static void SentimentAnalysis()
    {
        Scene currentScene = SceneManager.GetActiveScene();
        string entryText = (string)Variables.Scene(currentScene).Get("TempStringData");
        Debug.Log(entryText);

        string filePathName = Application.persistentDataPath;
        string entryPath = filePathName + "/entry.txt";


        //Write entry.txt for Python to access
        File.WriteAllText(entryPath, entryText);
        using (StreamWriter writetext = new("entry.txt"))
        {//may need to change back to WriteLine?
            writetext.Write(entryText);
        }
        
        string pythonScriptPath = Path.Combine(filePathName, "journal_sentiment.py");

        PythonRunner.RunFile(pythonScriptPath);
        Debug.Log("ran python");

        //Get analysis, set it to PlayerPrefs
        string analysis = PlayerPrefs.GetString("score");
        Variables.Scene(currentScene).Set("AnalysisResult", analysis);
        string compound = PlayerPrefs.GetString("compoundstring");
        Variables.Scene(currentScene).Set("scorestring", compound);

        //Store the entry for later
        string date = Variables.Scene(currentScene).Get("filefriendlydate").ToString();
        string time = Variables.Scene(currentScene).Get("filefriendlytime").ToString();
        string entryFilePath =  filePathName + "/" + date + time + "-entry.txt";
        string entryFileName = date + time + "-entry.txt";
        string results = PlayerPrefs.GetString("scoretextentry");

        string newEntryText = entryText + "\n" + analysis;

        File.WriteAllText(entryFilePath, newEntryText);
        using (StreamWriter writetext = new(entryFileName))
        {
            writetext.Write(newEntryText);
        }
   

        // Update is called once per frame
        //void Update()
        //{

        //}
    }
}