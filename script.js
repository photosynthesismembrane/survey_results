let currentIndex = 0;
const imagesPerPage = 10;
let selectedQuestions = [];
let image_folder = 'pinterest';
let image_data = survey_pinterest_two_options_data;
let questions = survey_questions;

// Load the image data
// const image_data = {/* content from reformatted_image_data.js */};
// Assuming image_data.js is already included in the HTML

// Function to shuffle array elements
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function truncateText(text, maxChars) {
    if (text.length <= maxChars) {
        return text;
    }
    let truncated = text.substring(0, maxChars);
    const lastSentenceEnd = Math.max(truncated.lastIndexOf('.'), truncated.lastIndexOf('!'), truncated.lastIndexOf('?'));
    if (lastSentenceEnd > -1) {
        truncated = truncated.substring(0, lastSentenceEnd + 1);
    } else {
        truncated = truncated.substring(0, truncated.lastIndexOf(' '));
    }
    return truncated.trim();
}

// Function to populate questions
function populateQuestions() {
    const questionsContainer = document.getElementById('questions-container');
    questionsContainer.innerHTML = `
            <!-- Questions will be populated here -->`;
    questions.forEach(questionObj => {
        const questionItem = document.createElement('div');
        questionItem.className = 'question-item';
        questionItem.innerText = questionObj.question;
        questionItem.onclick = () => handleQuestionClick(questionItem, questionObj.label);
        questionsContainer.appendChild(questionItem);
    });
}

// Handle question click
function handleQuestionClick(questionItem, questionLabel) {
    const previouslySelected = document.querySelector('.question-item.selected');
    if (previouslySelected) {
        previouslySelected.classList.remove('selected');
    }
    questionItem.classList.add('selected');
    selectedQuestions = [questionLabel];

    loadImages(currentIndex);
}

function changeDataSource() {
    let task = '';
    if (document.getElementById('two_options_radio_button').checked) {
        task = 'two_options';
    } else if (document.getElementById('highlights_radio_button').checked) {
        task = 'highlights';
    }
    const dataSource = document.getElementById('data-source').value;
    if (dataSource === 'pinterest') {
        image_folder = 'pinterest';
        if (task === 'two_options') {
            image_data = survey_pinterest_two_options_data;
        } else if (task === 'highlights') {
            image_data = survey_pinterest_highlighted_data;
        }
    } else if (dataSource === 'renaissance') {
        image_folder = 'renaissance';
        if (task === 'two_options') {
            image_data = survey_renaissance_two_options_data;
        } else if (task === 'highlights') {
            image_data = survey_renaissance_highlighted_data;
        }
    }
    populateQuestions();
    loadImages(currentIndex);
}


// Load images
function loadImages(startIndex) {
    // Check which one is selected of the radio buttons with the name task
    let task = '';
    if (document.getElementById('two_options_radio_button').checked) {
        task = 'two_options';
    } else if (document.getElementById('highlights_radio_button').checked) {
        task = 'highlights';
    }
    const dataSource = document.getElementById('data-source').value;
    if (task === 'two_options' && dataSource === 'pinterest') {
        image_data = survey_pinterest_two_options_data;
    } else if (task === 'highlights' && dataSource === 'pinterest') {
        image_data = survey_pinterest_highlighted_data;
    } else if (task === 'two_options' && dataSource === 'renaissance') {
        image_data = survey_renaissance_two_options_data;
    } else if (task === 'highlights' && dataSource === 'renaissance') {
        image_data = survey_renaissance_highlighted_data;
    }
    

    const imageContainer = document.getElementById('image-container');
    imageContainer.innerHTML = ''; // Clear previous images

    const imagesArray = Object.entries(image_data).map(([key, value]) => ({
        image_filename: key,
        ...value
    })).filter(image => !noDataForImage(image)).slice(startIndex, startIndex + imagesPerPage);

    function imageModelAnswersEmpty(image, model) {
        if  (!'llava_answers' in image) {
            return true;
        }

        // Check all selected questions whether there is at least one answer for the model
        return selectedQuestions.every(question => 
            !(image[`${model}_answers`] && question in image[`${model}_answers`] && image[`${model}_answers`][question])
        );
    }

    function noDataForImage(image) {
        if ((imageModelAnswersEmpty(image, 'llava')) && (imageModelAnswersEmpty(image, 'cogvlm')) && (imageModelAnswersEmpty(image, 'deepseek'))) {
            return true;
        }
        return false;
    }

    imagesArray.forEach((image, index) => {
        if (noDataForImage(image)) {
            return;
        }

        const imageWrapper = document.createElement('div');
        imageWrapper.className = 'image-wrapper';

        const imgElement = document.createElement('img');
        imgElement.src = `${image_folder}/${image.image_filename.replace(/(\.jpg).*/, '$1')}`;
        imgElement.alt = `Image ${startIndex + index + 1}`;
        imageWrapper.appendChild(imgElement);

        const answersDiv = document.createElement('div');
        answersDiv.className = 'answers';

        if (!imageModelAnswersEmpty(image, 'llava')) {
            const llavaDiv = document.createElement('div');
            text =  truncateText(selectedQuestions.map(question => image.llava_answers[question] || "N/A").join('<br>'), 1000);
            if (text.includes("<<voted>>")) {
                text = text.replace("<<voted>>", "");
                llavaDiv.className = 'answer-box voted';
            } else {
                llavaDiv.className = 'answer-box';
            }
            llavaDiv.innerHTML += `<p><strong>llava:</strong><br>${text}</p>`;
            answersDiv.appendChild(llavaDiv);
        }
        if (!imageModelAnswersEmpty(image, 'cogvlm')) {
            const cogvlmDiv = document.createElement('div');
            text = truncateText(selectedQuestions.map(question => image.cogvlm_answers[question] || "N/A").join('<br>'), 1000);
            if (text.includes("<<voted>>")) {
                text = text.replace("<<voted>>", "");
                cogvlmDiv.className = 'answer-box voted';
            } else {
                cogvlmDiv.className = 'answer-box';
            }
            cogvlmDiv.innerHTML += `<p><strong>cogvlm:</strong><br>${text}</p>`;
            answersDiv.appendChild(cogvlmDiv);
        }
        if (!imageModelAnswersEmpty(image, 'deepseek')) {
            const deepseekDiv = document.createElement('div');
            text = truncateText(selectedQuestions.map(question => image.deepseek_answers[question] || "N/A").join('<br>'), 1000);
            if (text.includes("<<voted>>")) {
                text = text.replace("<<voted>>", "");
                deepseekDiv.className = 'answer-box voted';
            } else {
                deepseekDiv.className = 'answer-box';
            }
            deepseekDiv.innerHTML += `<p><strong>deepseek:</strong><br>${text}</p>`;
            answersDiv.appendChild(deepseekDiv);
        }

        imageWrapper.appendChild(answersDiv);
        imageContainer.appendChild(imageWrapper);
    });
}

// Navigation functions
function loadPrevious() {
    if (currentIndex > 0) {
        currentIndex -= imagesPerPage;
        loadImages(currentIndex);
        scrollToFirstImage();
    }
}

function loadNext() {
    if (currentIndex + imagesPerPage < Object.keys(image_data).length) {
        currentIndex += imagesPerPage;
        loadImages(currentIndex);
        scrollToFirstImage();
    }
}

// Function to scroll to the first image
function scrollToFirstImage() {
    const firstImage = document.querySelector('#image-container img');
    if (firstImage) {
        firstImage.scrollIntoView({ behavior: 'smooth' });
    }
}


// Initialize
populateQuestions();

document.getElementById('two_options_radio_button').addEventListener('change', () => loadImages(currentIndex));
document.getElementById('highlights_radio_button').addEventListener('change', () => loadImages(currentIndex));
document.getElementById('data-source').addEventListener('change', changeDataSource);

loadImages(currentIndex);

