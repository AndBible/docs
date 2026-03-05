AI Bible Study Assistant
========================

|app| includes a built-in AI assistant that can translate, explain, summarize,
annotate, and perform word studies on Bible text. It works by sending selected
text to an external AI provider and displaying the result directly in the app.

.. note::

   The AI assistant requires an internet connection and an API key from a
   supported provider. Usage may incur costs depending on your chosen provider
   and model.

.. warning::

   When you use an AI prompt, the selected text is sent to your chosen external
   AI provider for processing. Do not use this feature with content you wish to
   keep private.


Getting Started
---------------

Choosing a Provider
^^^^^^^^^^^^^^^^^^^

|app| supports the following AI providers:

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Provider
     - Description
     - Notes
   * - **Google Gemini**
     - Google's AI models. Good starting point with a generous free tier.
     - Recommended for beginners
   * - **OpenAI (ChatGPT)**
     - The company behind ChatGPT.
     -
   * - **Anthropic (Claude)**
     - Maker of the Claude family of models.
     -
   * - **xAI (Grok)**
     - AI models from xAI.
     -
   * - **Mistral**
     - European AI provider with efficient models.
     -
   * - **DeepSeek**
     - Cost-effective models with strong multilingual capabilities.
     -
   * - **Groq**
     - Extremely fast inference with open-source models.
     -
   * - **Alibaba Cloud (Qwen)**
     - Chinese AI provider with multilingual models.
     -
   * - **OpenRouter**
     - Aggregator that provides access to models from many providers through a
       single API key.
     - Convenient for trying different models
   * - **Custom**
     - Connect to any OpenAI- or Anthropic-compatible API endpoint.
     - For self-hosted or other providers

If you are new to AI services, **Google Gemini** is a good starting point
because it offers a free usage tier that is sufficient for casual use.

Getting an API Key
^^^^^^^^^^^^^^^^^^

To use the AI assistant, you need an API key from your chosen provider:

#. Visit the provider's API key console (|app| provides direct links in the
   setup screen).
#. Create an account if you don't have one.
#. Generate a new API key.
#. Copy the key -- you will paste it into |app|.

.. note::

   API keys are stored securely on your device. They are **never** included
   in backups or synchronized to the cloud.

Adding a Provider
^^^^^^^^^^^^^^^^^

#. Open the top left main menu (|hamburger|).
#. Tap ``AI Settings``.
#. Tap ``Configure Connection``.
#. Tap ``Add provider``.
#. Select your provider from the list.
#. Paste your API key.
#. Choose a model (a sensible default is pre-selected).
#. Tap ``Save``.

The first provider you add becomes the default. You can change this later.

Multiple Providers
^^^^^^^^^^^^^^^^^^

You can configure multiple providers simultaneously. This is useful if you
want to use a cheaper model for simple tasks (like translation) and a more
capable model for complex tasks (like word studies).

The first provider is used by default. Individual prompts can be configured to
use a specific provider, overriding the default.


Using AI Prompts
----------------

Prompts are instructions that tell the AI what to do with your selected text.
|app| comes with several built-in prompts and allows you to create your own.

Built-in Prompts
^^^^^^^^^^^^^^^^

|app| includes six built-in prompts:

**Translate to [UI language]**
   Translates Bible text into the language your app interface is set to. If a
   translation in that language is already installed, it can use it directly
   instead of generating a new translation.

**Translate to English**
   Translates Bible text into English. Like the above, it can use an installed
   English Bible when available.

**Summary**
   Creates a concise summary of the selected passage with theological focus.

**Explain Verses**
   Explains the meaning, context, and theological significance of selected
   verses in depth.

**Strong's Annotation**
   Adds Strong's concordance numbers to Bible text by comparing it with a
   reference translation (KJV). Useful for translations that lack Strong's
   numbers.

**Word Study**
   Analyzes the original Hebrew or Greek words in the selected text, providing
   definitions, usage patterns, and links to dictionary entries.

Where Prompts Appear
^^^^^^^^^^^^^^^^^^^^

AI prompts are available in several places throughout the app. Each prompt is
configured to appear in the contexts where it is most useful:

**LLM Mode (document display)**
   Process an entire chapter or document through AI. Enable by selecting an
   LLM Mode prompt in the window's text display settings. The result replaces
   the document view.

**Verse selection**
   When you tap a verse and the verse action dialog appears, available AI
   prompts are shown as action buttons.

**Text selection**
   When you select text by long-pressing and dragging, AI prompts appear in the
   context menu.

**Window menu**
   Some prompts are accessible from the window's popup menu (long-press the
   window button at the bottom of the screen).

**Workspace menu**
   Some prompts appear in the workspace toolbar's three-dot menu.

**Note editor**
   When editing a bookmark note, AI prompts can assist with writing.

Running a Prompt
^^^^^^^^^^^^^^^^

**Example: Explaining a verse**

#. Tap a verse to open the verse action dialog.
#. Tap the ``Explain Verses`` button.
#. The AI processes your request and displays the result.

**Example: Using LLM Mode for a whole chapter**

#. Long-press the window button at the bottom of the screen.
#. Tap ``Text Options``, then ``All Text Options``.
#. Under the LLM Mode section, select a prompt (e.g. ``Translate``).
#. The entire chapter is processed through the selected prompt.

**Example: Word study on selected text**

#. Long-press a word in the Bible text to start a text selection.
#. Extend the selection if needed.
#. Tap ``Word Study`` from the context menu.

The Agent Log
^^^^^^^^^^^^^

When an AI prompt runs, a log panel shows the progress in real time. You can
see:

* Which tools the AI is calling (e.g. reading verses, looking up dictionaries)
* Permission requests for write operations
* Token usage and estimated cost

You can cancel a running prompt at any time by tapping the cancel button.


AI Tools
--------

AI prompts can use *tools* -- specialized functions that let the AI read data
from your app or make changes. This is what allows the AI to look up cross-
references, search your Bible, read your bookmarks, and more.

Read Tools
^^^^^^^^^^

Read tools retrieve information without making any changes. They do not require
permission.

* **Read verse content** -- Retrieve the text of any verse or chapter from any
  installed Bible translation.
* **Search Bible** -- Search for verses containing specific keywords.
* **Read commentaries** -- Look up commentary on specific verses from installed
  commentary modules.
* **Look up dictionary entry** -- Look up entries in installed dictionaries and
  lexicons (e.g. Strong's, Robinson's).
* **Get bookmarks for verse** -- Retrieve your bookmarks at a specific verse.
* **Get bookmarks with label** -- Get all bookmarks assigned to a specific label.
* **List all labels** -- Get a list of all your labels.
* **Read study pad content** -- Read entries from a study pad.
* **Search study pads** -- Search study pad entries by keyword.
* **List installed documents** -- Get a list of installed Bibles, commentaries,
  and dictionaries.

Write Tools
^^^^^^^^^^^

Write tools can create or modify data in your app. They are subject to the
:ref:`ai:Permissions` system.

* **Create bookmark** -- Create a new bookmark at a verse, optionally with a
  note.
* **Add bookmark note** -- Add a note to an existing bookmark.
* **Update bookmark note** -- Modify an existing bookmark's note.
* **Create label** -- Create a new label for organizing bookmarks and study pads.
* **Add label to bookmark** -- Assign a label to a bookmark.
* **Add study pad entry** -- Add a text entry to a study pad.
* **Set document title** -- Set the title for an AI-generated document.
* **Open study pad** -- Complete the task and open a specified study pad.
* **Finish without document** -- End the task without producing a document
  (for action-only prompts that create bookmarks, etc.).


Permissions
-----------

Write tools require your permission before the AI can use them. This ensures
the AI cannot modify your data without your knowledge.

.. note::

   Read tools never require permission. Only write tools (creating bookmarks,
   adding notes, etc.) are gated by the permission system.

Permission Modes
^^^^^^^^^^^^^^^^

There are four permission modes:

**Always ask** (default)
   The AI asks for your permission every time it wants to use a write tool.
   A dialog shows what the tool will do and lets you approve or deny.

**Ask once per run**
   The AI asks permission the first time it uses a write tool during a prompt
   run. After you approve, subsequent write operations in the same run proceed
   without asking.

**Allow all**
   All write operations are allowed automatically without asking. Use this only
   if you fully trust the prompt.

**Deny all**
   All write operations are denied automatically. The AI can only read data.

Setting Permissions
^^^^^^^^^^^^^^^^^^^

Permissions can be configured at three levels:

#. **Global default** -- In ``AI Settings`` > ``Configure Connection`` >
   ``Manage tool permissions``. This sets the default behavior for all prompts.
#. **Per-prompt** -- When editing a custom prompt, you can set a permission mode
   that overrides the global default for that prompt.
#. **Per-tool** -- In the global tool permissions dialog, you can set individual
   tools to "Always allow" or "Always deny", overriding the mode-based
   behavior.


Custom Prompts
--------------

Creating a Custom Prompt
^^^^^^^^^^^^^^^^^^^^^^^^

You can create your own prompts for specialized tasks:

#. Open the top left main menu (|hamburger|).
#. Tap ``AI Settings``.
#. Tap the ``+`` button.
#. Fill in the prompt details:

   * **Name** -- A short name shown in menus.
   * **Description** -- What the prompt does (shown in the prompt list).
   * **Template** -- The instructions sent to the AI. This is the core of your
     prompt.
   * **Contexts** -- Where this prompt should appear (verse selection, text
     selection, window menu, etc.).
   * **Provider and model** -- Optionally override which provider and model to
     use for this prompt.

#. Tap ``Save``.

Editing Built-in Prompts
^^^^^^^^^^^^^^^^^^^^^^^^^

Built-in prompts cannot be modified directly. To customize one:

#. Open the built-in prompt you want to modify.
#. Use the ``Copy to customize`` option.
#. Edit the copy as needed and save.

Prompt Template Tips
^^^^^^^^^^^^^^^^^^^^

* **Be specific** -- Clearly describe what you want the AI to do and what
  format the output should be in.
* **Mention tools** -- If you want the AI to look up commentaries or
  dictionaries, mention it in the prompt. For example: "Look up relevant
  commentary entries to support your explanation."
* **Define the output format** -- Specify whether you want bullet points,
  paragraphs, a table, or other formats.
* **Set the language** -- If you want output in a specific language, say so
  explicitly.

Sharing Prompts (CSV)
^^^^^^^^^^^^^^^^^^^^^

Custom prompts can be exported and imported as CSV files, making it easy to
share your prompts with other |app| users:

* **Export** -- From the prompt list, use the export option to save your custom
  prompts to a CSV file.
* **Import** -- Use the import option to load prompts from a CSV file.


Cache and Cost Management
-------------------------

Cache
^^^^^

AI results are cached locally so that the same request does not consume
additional API tokens. For example, if you translate Genesis 1 and then
navigate away and come back, the cached result is displayed instantly.

The cache can be managed in ``AI Settings`` > ``Configure Connection`` >
``Cache``:

* **Browse** cached entries with details (document, verse, prompt type, model,
  date, size).
* **Filter** by document, processing type, or model.
* **Delete** entries individually, by filter, by age (older than 7, 30, or 90
  days), or all at once.

.. note::

   The cache is stored only on the device and is not synchronized to the cloud.

Cost Tracking
^^^^^^^^^^^^^

|app| tracks token usage and provides estimated costs for each provider:

* **Token counts** -- Input tokens (text sent to the AI), output tokens
  (text received), and cache tokens are tracked separately.
* **Estimated cost** -- Calculated based on each model's published pricing.
* **Per-provider breakdown** -- Each configured provider shows its own usage
  and cost.
* **Reset** -- You can reset the usage counters at any time.

View cost tracking in ``AI Settings`` > ``Configure Connection`` under the
Usage section.

.. note::

   Cost estimates are approximate. Always check your provider's billing
   dashboard for actual charges.


Cloud Sync
----------

When :doc:`cloud_sync` is enabled, the following AI data is synchronized:

* **Synced:** Custom prompts and provider configurations (provider type,
  model selection, endpoint settings).
* **Not synced:** API keys, cache, and usage/cost data.

API keys remain on each device for security. You need to enter your API key
separately on each device.


Tips and Troubleshooting
-------------------------

Recommended Setup for Beginners
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Start with **Google Gemini** -- it has a free tier that is sufficient for
   trying out the AI features.
#. Try the **Explain Verses** prompt first -- tap a verse and select it from
   the verse action dialog.
#. Keep the permission mode set to **Always ask** until you are comfortable
   with how the AI uses tools.

Reducing Costs
^^^^^^^^^^^^^^

* Use a smaller, cheaper model for simple tasks like translation.
* Use a more capable (and expensive) model only for complex tasks like word
  studies.
* Configure multiple providers and assign them to specific prompts.
* The cache prevents duplicate API calls -- avoid clearing it unnecessarily.

Common Issues
^^^^^^^^^^^^^

**"API key invalid" or authentication errors**
   Double-check that your API key is entered correctly. Visit your provider's
   console to verify the key is active.

**Slow responses or timeouts**
   AI responses can take several seconds, especially for longer passages or
   complex prompts. Check your internet connection if responses consistently
   fail.

**Unexpected or low-quality results**
   Try a more capable model, or refine your prompt to be more specific about
   what you want. Different models have different strengths.

**Higher costs than expected**
   Check which model you are using -- larger models cost significantly more.
   Review the cost tracking in AI Settings to identify which prompts consume
   the most tokens. Consider switching to a smaller model for routine tasks.
