document.addEventListener('DOMContentLoaded', () => {
    const modeSelect = document.getElementById('mode');
    const generalFields = document.getElementById('general-fields');
    const detailedFields = document.getElementById('detailed-fields');
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    // Function to toggle required and disabled attributes
    function toggleFieldAttributes(showFields, hideFields) {
        // Enable and set required for visible fields
        showFields.querySelectorAll('input, select').forEach(field => {
            field.removeAttribute('disabled');
            field.setAttribute('required', '');
        });

        // Disable and remove required for hidden fields
        hideFields.querySelectorAll('input, select').forEach(field => {
            field.setAttribute('disabled', '');
            field.removeAttribute('required');
        });
    }

    modeSelect.addEventListener('change', () => {
        if (modeSelect.value === 'general') {
            generalFields.classList.remove('hidden');
            detailedFields.classList.add('hidden');
            toggleFieldAttributes(generalFields, detailedFields);
        } else {
            generalFields.classList.add('hidden');
            detailedFields.classList.remove('hidden');
            toggleFieldAttributes(detailedFields, generalFields);
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent default form submission behavior

        const formData = new FormData(form); // Collect form data
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Failed to fetch prediction');
            }

            const data = await response.json();
            resultDiv.textContent = `Prediction: ${data.prediction}`;
            resultDiv.classList.remove('hidden');
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
            resultDiv.classList.remove('hidden');
        }
    });
});
