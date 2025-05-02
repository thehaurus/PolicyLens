# 🧠 AI Policy Understanding Assistant

Policy Understanding Assistant is an AI-powered multi-agent system that reads complex insurance policy PDFs, simplifies them into plain English, answers user questions contextually, and personalizes responses based on the user's profile — all through a LangGraph + LangChain-powered agentic workflow with a Streamlit interface.

---

## 💡 Why This?

Insurance policies are complex and confusing.  
Clients and customers constantly ask:

- ❓ “What’s my deductible?”
- ❓ “Am I covered for this?”
- ❓ “What does this legal clause mean?”

This system **automates the job of a policy advisor**, providing accurate, plain-English answers from real PDF documents.

---

## 📄 Sample Input

![image alt](https://github.com/imayushthakur/PolicyLens/blob/main/examples/Input/Input.PNG?raw=true)

## 📄 Sample Output

![image alt](https://github.com/imayushthakur/PolicyLens/blob/main/examples/Output/output_1_answer.PNG?raw=true)

![image alt](https://github.com/imayushthakur/PolicyLens/blob/main/examples/Output/output_2_personalized_tip.PNG?raw=true)

## 🎯 Use Cases

- 📑 Insurance companies automating support
- 💼 HR departments explaining benefit plans
- 📄 Legal tech products offering contract intelligence
- 🤖 AI Agents that understand real-world policies

## 🧠 What It Does

This system uses a **multi-agent architecture** built with LangGraph to simulate human-like understanding and interaction:

| 🧩 Agent                      | Description                                                    |
| ----------------------------- | -------------------------------------------------------------- |
| 📄 **Document Parsing Agent** | Extracts key information from uploaded insurance policy PDFs   |
| ✍️ **Simplification Agent**   | Translates policy language into plain English                  |
| 🤖 **Query Handling Agent**   | Answers user questions contextually from the document          |
| 🎯 **Personalization Agent**  | Tailors the answer based on user profile (age, location, plan) |
| 🔁 **Feedback Agent**         | Collects user satisfaction to improve future interactions      |

---

```bash
git clone https://github.com/imayushthakur/PolicyLens.git
cd PolicyLens
pip install -r requirements.txt
streamlit run streamlit_app.py

```

💡 Let's collaborate! Reach out via email to discuss how I can help bring your ideas to life.

📬 Contact Me 📧 Email: thehaurusai@gmail.com

Built with ❤️ using cutting-edge AI technologies! Let’s create something amazing together! 🚀
