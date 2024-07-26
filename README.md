# Software Architecture-based Self-adaptation in Robotics
This repository is a companion page for the following (pending) publication:
Alberts, E., Gerostathopoulos, I., Malavolta, I., Hernández Corbato, C., & Lago, P. 2024. Software Architecture-Based Self-Adaptation in Robotics. SSRN

It contains all the material required for replicating the study, including: a script to re-do the proceedings collection, title keyword filtering, and generate the plots.

## How to cite us
The scientific article describing design, execution, and main results of this study is available [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4805883).<br> 
If this study is helping your research, consider to cite it is as follows, thanks!

```
@article{alberts2024software,
  title={Software Architecture-Based Self-Adaptation in Robotics},
  author={Alberts, Elvin and Gerostathopoulos, Ilias and Malavolta, Ivano and Hern{\'a}ndez Corbato, Carlos and Lago, Patricia},
  journal={Available at SSRN 4805883}
  year={2024}
}
```

### Getting started
0. If you are not interested in any of the details, and would simply like to reproduce everything (except the horizontal analysis and including safely installing dependencies), we provide a shell script to do so, simply run `./everything.sh`, on a unix-based system. For your convenience, if you are using Windows we provide an `everything.bat` script to run instead. For either version, you only need to pass the keyword which refers to python3 on your system as an argument, so either `--python3` if you use python 3 by typing `python3` or `--python` if you use `python` to use python 3. 

1. This reproduction package relies (only) on Python. Please see that you have Python 3 installed on your system. Then, you can choose to create a virtual environment, or simply run  `pip install -r requirements.txt` in the root folder of this repository after you have cloned it. We are unaware of any version conflicts, and presume most installable versions of each python dependency should work.

2. The reproduction package revolves around three scripts: proceedings_collection.py, pilots_and_final.py, and generate_plots.py. Every script can be run by opening a terminal in the root of the repository and typing some form of `python src/script_name.py`, for example `python src/proceedings_collection.py`. Keep in mind on some system you may have to specify python3, so `python3 src/script_name.py`.

3. Here we will cover proceedings_collection.py. This script parses the XML of the dblp snapshot, and collected potentially-relevant studies in accordance with the procedure and time criteria outlined in our study. There are two arguments/options that can be passed to the script `--all` and `--pilot`. The first option, `--all` means we collect every single study without filtering by their titles. This allows the user to try different keywords manually to determine how many studies this may result in, and aids in the transparency of the filtering process. By default, the title keyword filtering is applied if the `--all` option is not specified. The second option `--pilot` produces the .csv of potentially-relevant as it was used for the pilot studies. This distinction exists as between the pilot studies and the final selection we uncovered that the proceedings of some years of the SEAMS conference which we target, are misleadingly categorized under the ICSE conference (with which it is co-located) which we do not target. We remedied this after the pilot, meaning the seeded randomized extraction of potentially-relevant studies was no longer reproducible without maintaining these two distinct versions.

4. For pilots_and_final.py to be able to use this script fully, it requires having run the proceedings_collection.py script prior. In this branch of the repository, it is only possible to generate the new selection round after the study has been updated to include 2023-June 2024. For instructions on generating the pilot selections and original final selection please see the other branch.

5. For generate_plots.py this script generates a bar plot for every data parameter from the vertical analysis. This will generate all those found in our paper, but also those we did not include but use to report on the results. There is one option which can be passed to this script `--show` this makes it so that the plots are displayed to the user one by one rather than saved in a folder called plots. This is useful if you are modifying the script and would not like to overwrite previous versions of the plots.

6. For the horizontal_synthesis we provide a simple R script. If you would like to use the script you of course need a working installation of R (https://cran.r-project.org/) and to first install its dependencies.
### Snowballing
The snowballing was done semi-manually. For forward snowballing we used Google Scholar to find all the papers which cite ours, manually recording the DOI and title of each study and removing duplicates.
For the backwards snowballing, we made use of https://github.com/helenocampos/PDFReferencesExtractor, and corrected any mistakes, and used tools such as Zotero to grab the missing DOIs from titles when this occurred. 