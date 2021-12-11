# Kwe'

Fun, engaging and interactive app for kids to learn the Mi'kmaq language.

**Software Engineering (CSCI-3428) Project for Fall 2021**
at
**Saint Mary's University, Halifax, NS, Canada**
by
Isaiah Jarvis
Jacob White
Kyle Coleman-Sadd
Naziya Tasnim
Sheikh Saad Abdullah

Files to be put on the public server.

The website can be accessed at [https://ugdev.cs.smu.ca/~group15/](https://ugdev.cs.smu.ca/~group15/) for general use.

---

## Installation and Updating

1. Log in to the `group15` account on the `ugdev.cs.smu.ca` server

2. Run the following command:

```bash
bash -c "$(curl -fsSL https://kwe.cybar.dev/install.sh)"
```

3. Wait for the command to finish running (the prompt will appear again)

- Done

---

## Run the App

1. Open a web browser (Safari, Edge, Firefox, etc.)

2. In the browser search bar, type or paste the following URL:<br />
[https://ugdev.cs.smu.ca/~group15/](https://ugdev.cs.smu.ca/~group15/)

3. Press the Enter/Return key

- Done

---

## Change dialogue audio

*Prerequisites: [Ren'Py](https://renpy.org/), [git](https://git-scm.com/), Terminal (cmd.exe, iTerm, etc.), internet connection*

1. Open the Terminal application

2. Type or paste the following command:<br />
`git clone https://github.com/HealthSouthern48/KLOQOWEJ.git`

3. Open your File Browser and navigate to the downloaded folder

4. Navigate to the `scripts` folder inside the `game` folder inside the folder named `KLOQOWEJ`

5. The files are named in the format `chapX`, where `X` is the chapter number. Open the file for the chapter whose dialogue you wish to change

6. Look for the dialogue whose audio you wish to change.<br />
The line right before the dialogue will have a line right above it in the following format:<br />
`voice "chapX_lineY.mp3"`<br />
Where X is the chapter number and Y is the dialogue number. That is the name of the file that needs to be changed.

7. Navigate to the `audio` folder inside the `game` folder inside the folder named `KLOQOWEJ`

8. Replace the file you wish to change with your desired audio file.<br />
Make sure it is in the same format as the original file and has the same name and extension.

9. Open Ren'Py and navigate to Preferences

10. Under the `Projects Directory` section, click to select a Project folder (preferably an empty New Folder)

11. Click `Return`

12. In your File Browser, Move the `KLOQOWEJ` folder into the Project folder selected in the previous step

13. In Ren'Py, click `KLOQOWEJ` under the `PROJECTS` section

14. Click `Web` under the `Actions` section

15. Click `Build Web Application` and wait for the process to finish

16. Close Ren'Py

17. Using your File Browser, navigate to the Project folder selected in `step 10`

18. Open the folder `KLOQOWEJ-1.0-web` inside the folder `KLOQOWEJ-1.0-dists` inside the Project folder

19. Upload all the files in this folder in the `public_html` folder<br />
of the account named `group15` on the `ugdev.cs.smu.ca` server,<br />
overwriting the existing files with the same name

20. Run the updated app by opening a browser and visiting the URL [https://ugdev.cs.smu.ca/~group15/](https://ugdev.cs.smu.ca/~group15/)

- Done.

---

## credits:

Background art: [Background vector created by vectorpouch - www.freepik.com](https://www.freepik.com/vectors/background)
