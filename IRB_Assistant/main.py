import warnings

import typer

from IRB_Assistant import prompts
from IRB_Assistant.generate import get_irb_assistant_response
from IRB_Assistant_config import config

# Initialize Typer CLI app
app = typer.Typer()
warnings.filterwarnings("ignore")


@app.command()
def generate_irb(
    hypothesis: str, inclusion: str, time_window: str, exclusion: str, design: str, details: str
):
    """
    The function `generate_irb` takes in various parameters related to an IRB (Institutional Review
    Board) application and returns a response from an IRB assistant.

    Args:
      hypothesis (str): A statement or prediction that you want to test or investigate.
      inclusion (str): The "inclusion" parameter refers to the criteria that participants must meet in
    order to be included in the study. It specifies the characteristics or conditions that individuals
    must possess in order to be eligible for participation.
      time_window (str): The `time_window` parameter is used to specify the duration or time frame for
    the research study. It can be a specific time period, such as "6 months" or "1 year", or it can be a
    more general description, such as "longitudinal study" or "cross-sectional
      exclusion (str): The "exclusion" parameter is used to specify any criteria or factors that would
    exclude certain individuals or groups from participating in the study. This could include things
    like age restrictions, medical conditions, or other specific characteristics that would make someone
    ineligible for the study.
      design (str): The "design" parameter refers to the design of the research study. It specifies the
    overall plan or strategy that will be used to answer the research question or test the hypothesis.
    Examples of different research designs include experimental, observational, correlational, and
    qualitative designs.
      details (str): The "details" parameter is a string that contains additional information or
    specifications related to the IRB (Institutional Review Board) application. It can include any
    relevant details such as the study population, data collection methods, ethical considerations, or
    any other information that is important for the IRB review process

    Returns:
      The function `generate_irb` returns the contents of the response generated by the IRB assistant.
    """

    result = get_irb_assistant_response(
        hypothesis=hypothesis,
        inclusion=inclusion,
        time_window=time_window,
        exclusion=exclusion,
        design=design,
        details=details,
        chat=config.CHAT,
        chat_prompt=prompts.irb_chat_prompt,
    )

    return result.contents


if __name__ == "__main__":
    app()  # pragma: no cover, live app