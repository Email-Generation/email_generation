import { useRef, useState } from "react";
import useAutosizeTextArea from "./useAutosizeTextArea";
import SkeletonLoader from "./skelotonLoader";
import "./App.css";

export default function App() {
  const [emailPrompt, setEmailPrompt] = useState("");
  const [emailResponse, setEmailResponse] = useState("")
  const [requestSent, setRequestSent] = useState(false)
  const textAreaRef = useRef(null);

  useAutosizeTextArea(textAreaRef.current, emailPrompt);

  const handleChange = (evt) => {
    const val = evt.target?.value;
    setEmailPrompt(val);
  };

  const getEmailResponse = async (text) => {
    var email_response = await fetch(
      "http://127.0.0.1:8000/emails/",
      {
        method: 'POST',
        body: JSON.stringify({ email_prompt: text }),
        headers: { 'Content-Type': 'application/json' }
      }
    )
    let res = await email_response.json()
    setRequestSent(false)
    res = res.replace("\n", "<br>")
    res = StringToHtml(res)
    return res
  }

  const StringToHtml = (text) => {
    return (
      <div dangerouslySetInnerHTML={{ __html: text }}></div>
    )
  }

  return (
    <div className="App">
      <header
        style={{ margin: 10 }}
      >
        Auto generate personalised email sequences
      </header>

      <div style={{
        alignItems: "center",
        alignContent: "center",
        verticalAlign: "center",
        justifyContent: "center"
      }}>
        <textarea
          onChange={handleChange}
          placeholder="Write the email prompt"
          ref={textAreaRef}
          rows={emailPrompt === "" ? 2 : 1}
          cols={75}
          style={{
            borderRadius: 5
          }}
          value={emailPrompt}
        />

        <button 
          className="styledButton"
          type="submit"
          onClick={async () => { setEmailResponse(""); setRequestSent(true); setEmailResponse(await getEmailResponse(emailPrompt)) }}
        >
          Send
        </button>
      </div>

      <div
        style={{
          width: "80%",
        }}
      >
        {
          requestSent === true && emailResponse === ""? 
            <SkeletonLoader/> : 
              (
              requestSent === false && emailResponse !== "" ? 
                <div style={{ backgroundColor: "white", width: "100%", height: "600px", borderRadius: 10, marginTop: 10, color: "black", overflowY: "scroll", overflowX: "hidden" }}>
                  {emailResponse}
                </div> : null
              )
        }
      </div>
    </div>
  );
}
