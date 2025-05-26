import wixData from 'wix-data';

$w.onReady(function () {
  $w("#submitBtn").onClick(() => {
    const answers = {
      q1: $w("#dropdown1").value,
      q2: $w("#dropdown2").value,
      q3: $w("#dropdown3").value
    };

    const tags = generateTags(answers);

    wixData.insert("userResponses", {
      userId: wixUsers.currentUser.id,
      answers: answers,
      tags: tags.join(",")
    }).then(() => {
      wixLocation.to(`/recommendation-page?tags=${tags.join(",")}`);
    });
  });
});

// 🧠 根據測驗答案產生標籤（簡化版）
function generateTags(answers) {
  const tags = [];
  if (answers.q1 === "藝術") tags.push("art");
  if (answers.q2 === "科技") tags.push("tech");
  if (answers.q3 === "音樂") tags.push("music");
  return tags;
}
