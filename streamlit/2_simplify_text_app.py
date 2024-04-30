from llm_utils.streamlit_common import apply_uab_font, hide_streamlit_branding
import IRB_Assistant.generate as irb_generate
import IRB_Assistant.prompts as irb_assistant_prompts
import streamlit as st
# TODO: add documentation
# TODO: move markdown of collaborators to llm_utils and config
def show_simplify_text_page():
    # page metadata
    st.set_page_config(
        page_title="Simplify Text",
        page_icon="🔠",
    )
    # hide streamlit branding
    hide_streamlit_branding()


    # apply uab font
    apply_uab_font()

    # page content
    st.title("🔠 Text Simplifier 🤖")
    st.markdown(
        """
    **Simplify clinical, research, or regulatory text to an 8th-grade reading level**

    Brought to you by the Anesthesiology Research Support, Informatics, and Data Science teams.

    _Not approved for use with PHI._

    All submissions are recorded for potential review by departmental and health system personnel.

    ---
    """
    )


    with st.form(key="simplify_form"):
        text_to_simplify = st.text_area(
            "Text to simplify:",
            """The efficacy of the treatment was assessed using a double-blind, placebo-controlled study. Participants were randomized into two groups, with one group receiving the experimental drug, while the other group was administered a placebo. Primary endpoints of the study included overall survival (OS) and progression-free survival (PFS). The drug demonstrated an increased median survival, and side effects were minor and transient, indicating the potential therapeutic value of the drug in clinical applications. However, a comprehensive interpretation of these results necessitates further investigation, particularly to determine the long-term effects of the treatment and its efficacy in a larger, more diverse population.
                                        """,
            height=400,
        )
        submit_comparison_button = st.form_submit_button("Simplify")
        if submit_comparison_button:
            with st.spinner("Thinking..."):
                result, _ = irb_generate.generate_simplified_text(
                    text_to_simplify,
                    chat_config=st.session_state.chat_config,
                    chat_prompt=irb_assistant_prompts.simplify_chat_prompt,
                )
            st.markdown(result.content)

       

if __name__ == "__main__":
    show_simplify_text_page()
