# streamlit_app.py

import os
from datetime import datetime

from llm_utils.database import get_db_connection
from llm_utils.streamlit_common import apply_uab_font, hide_streamlit_branding

import IRB_Assistant.generate as irb_generate
import IRB_Assistant.prompts as irb_assistant_prompts
import IRB_Assistant_config.app_config as irb_assistant_app_config
import IRB_Assistant_config.config as irb_Assistant_config
import streamlit as st


def show_simplify_text_page():
    os.environ["OPENAI_API_KEY"] = irb_assistant_app_config.OPENAI_API_KEY
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
                submit_time = datetime.now()
                result, response_meta = irb_generate.generate_simplified_text(
                    text_to_simplify,
                    chat=irb_Assistant_config.CHAT,
                    chat_prompt=irb_assistant_prompts.simplify_chat_prompt,
                )
                response_time = datetime.now()
            st.markdown(result.content)

            try:
                with get_db_connection(
                    db_server=irb_assistant_app_config.DB_SERVER,
                    db_name=irb_assistant_app_config.DB_NAME,
                    db_user=irb_assistant_app_config.DB_USER,
                    db_password=irb_assistant_app_config.DB_PASSWORD,
                ) as conn:
                    # tempting to move this into llm_utils, but the query will be unique to each app.
                    cursor = conn.cursor()
                    query = """
                    INSERT INTO [dbo].[text_simplifier] (
                        complex_text, 
                        simplified_text, 
                        input_time, 
                        response_time,
                        total_cost
                    ) VALUES (?, ?, ?, ?, ?)
                    """

                    cursor.execute(
                        query,
                        (
                            text_to_simplify,
                            result.content,
                            submit_time,
                            response_time,
                            response_meta.total_cost,
                        ),
                    )

                st.success(
                    "To comply with a Health System Information Security request, submissions are recorded for potential review."
                )
            except Exception as e:
                st.error(
                    "Something went wrong, and your submission was not recorded for review. Give the following message when asking for help."
                )
                st.error(e)


if __name__ == "__main__":
    show_simplify_text_page()
