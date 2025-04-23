# NZDedupeCheck
Checks quality of matching between records in CF NZ Dedupe Report<br />
<br />
Inputs:<br />
&bull;NZ Dedupe Report in .csv <i>sorted by Identifier!</i><br />
<i>NOTE: Requires columns for Title, Publication Date, Language Of Cataloging, Author, ISBN (Normalized), Edition, and Publisher, along with standard columns. Use KB - NZ Dedupe Report with Comparison Fields template available in NZ Analytics instance.</i><br />
<br />
Outputs:<br />
&bull;Report with confidence next to all records with matching values in Identifier column<br />
<br />
Process:<br />
&bull;Prompts for file using tkinter filedialog<br />
&bull;Compares adjacent rows on value in Identifier column (file must be sorted by Identifier to ensure matches are adjacent)<br />
&bull;If a match is found, compares key fields (Title, Publication Date, Language Of Cataloging, Author, ISBN (Normalized), Edition, and Publisher) using fuzz.WRatio<br />
&bull;Adds a column for Similarity, populated with the average of all comparison fields or 0 if no matching record found<br />
&bull;Saves the output as a file with a unique name using date and time<br />
<br />
Dependencies:<br />
&bull;Pandas>br />
&bull;FuzzyWuzzy<br />
&bull;NumPy<br />
&bull;DateTime<br />
&bull;TKinter<br />
&bull;Time<br />
