document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    const generatedHTML = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>${title}</title>
        </head>
        <body>
            <header>
                <h1>${title}</h1>
            </header>
            <main>
                ${content}
            </main>
        </body>
        </html>
    `;

    const newWindow = window.open();
    newWindow.document.write(generatedHTML);
});
